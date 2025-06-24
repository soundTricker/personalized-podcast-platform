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

import {Navbar, Button, NavbarBrand, Avatar, Dropdown} from 'flowbite-react';
import { Link } from 'react-router';
import { useAuth } from '../firebase/auth';
import { useRef, useState, useEffect } from 'react';

/**
 * Global header component for the application
 */
export default function Header() {
  const { currentUser, logout } = useAuth();
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Handle click outside to close dropdown
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsDropdownOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  // Handle logout
  const handleLogout = async () => {
    try {
      await logout();
      setIsDropdownOpen(false);
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <Navbar fluid className="w-full border-b border-gray-200 bg-white py-2 shadow-sm">
      <div className="w-full mx-auto flex flex-wrap items-center justify-between">
        <NavbarBrand as={Link} to="/">
          <div className="flex flex-row items-center gap-1">
            <img className="inline-block h-8" src="/ppp_logo.jpeg" alt="Personalized Podcast Platform"></img>
            <span className="self-center whitespace-nowrap text-xl font-semibold">
             PPP
          </span>
          </div>

        </NavbarBrand>
        <div className="flex items-center gap-3">
          <Button as={Link} to="/listener-programs" color="light">
            プログラム一覧
          </Button>

          {currentUser && (
            <div className="relative" ref={dropdownRef}>
              <div 
                className="cursor-pointer"
                onClick={() => setIsDropdownOpen(!isDropdownOpen)}
              >
                <Avatar 
                  rounded 
                  alt="User avatar" 
                  img={currentUser.photoURL || undefined}
                  placeholderInitials={currentUser.displayName ? currentUser.displayName.charAt(0).toUpperCase() : 'U'}
                />
              </div>

              {isDropdownOpen && (
                <div className="absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-10">
                  <div className="py-1">
                    <button
                      onClick={handleLogout}
                      className="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                    >
                      ログアウト
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </Navbar>
  );
}
