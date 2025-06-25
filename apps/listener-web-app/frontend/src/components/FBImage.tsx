/**
 * Copyright 2025 Keisuke Tominaga a.k.a soundTricker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {useEffect, useState} from 'react';
import {getDownloadURL, getStorage, ref} from 'firebase/storage';

// Initialize Firebase app for storage
const storage = getStorage();

interface FBImageProps {
  path: string | null | undefined;
  alt?: string;
  className?: string;
  width?: number;
  height?: number;
}

/**
 * FBImage component that displays images from Firebase Storage
 * Shows /noimage.png as fallback while loading or if path is empty
 */
export default function FBImage({ path, alt = '', className, width, height }: FBImageProps) {
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    if (!path) {
      setLoading(false);
      setError(false);
      setDownloadUrl(null);
      return;
    }

    const fetchDownloadUrl = async () => {
      try {
        setLoading(true);
        setError(false);
        
        // Create a reference to the file
        const imageRef = ref(storage, path);
        
        // Get the download URL
        const url = await getDownloadURL(imageRef);
        setDownloadUrl(url);
      } catch (err) {
        console.error('Error getting download URL:', err);
        setError(true);
      } finally {
        setLoading(false);
      }
    };

    fetchDownloadUrl();
  }, [path]);

  // Show fallback image if no path, loading, or error
  const shouldShowFallback = !path || loading || error || !downloadUrl;
  const imageSrc = shouldShowFallback ? '/noimage.png' : downloadUrl;

  return (
    <img
      src={imageSrc}
      alt={alt}
      className={className}
      width={width}
      height={height}
      onError={() => {
        // If the download URL fails to load, show fallback
        if (!shouldShowFallback) {
          setError(true);
        }
      }}
    />
  );
}