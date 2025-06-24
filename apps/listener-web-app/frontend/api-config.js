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

// Script to configure API base URL from environment variables
// This script is executed at container startup

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import * as glob from 'glob';

// Get API URL from environment variable or use default
const API_URL = process.env.API_URL || '';

console.log(`Configuring API base URL: ${API_URL}`);

// Get the directory name equivalent to __dirname in CommonJS
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to the OpenAPI configuration file
const openApiConfigPath = path.join(__dirname, 'build', 'client', 'assets', 'OpenAPI-*.js');

// Find the OpenAPI configuration file using glob pattern
const files = glob.sync(openApiConfigPath);

if (files.length === 0) {
  console.error('OpenAPI configuration file not found');
  process.exit(1);
}

const configFile = files[0];
console.log(`Found OpenAPI configuration file: ${configFile}`);

// Read the file content
let content = fs.readFileSync(configFile, 'utf8');

// Replace the BASE property
content = content.replace(/BASE:\s*['"].*?['"]/g, `BASE: '${API_URL}'`);

// Write the updated content back to the file
fs.writeFileSync(configFile, content);

console.log('OpenAPI configuration updated successfully');
