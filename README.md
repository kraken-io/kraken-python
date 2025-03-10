Official Kraken.io library for Python
===========

With this Python Client you can plug into the power and speed of [Kraken.io](http://kraken.io/) Image Optimizer.

## Important Notice

As of version **0.2.0**, this package **only supports Python 3.8 and later**. If you are using an older Python version, please install an earlier (<=0.1.0) version of this package.

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Downloading Images](#downloading-images)
* [How To Use](#how-to-use)
* [Wait and Callback URL](#wait-and-callback-url)
  * [Wait Option](#wait-option)
  * [Callback URL](#callback-url)
* [Authentication](#authentication)
* [Usage - Image URL](#usage---image-url)
* [Usage - Image Upload](#usage---image-upload)
* [Usage - User status](#usage---user-status)
* [Lossy Optimization](#lossy-optimization)
* [Image Resizing](#image-resizing)
* [WebP Compression](#webp-compression)
* [PDF Compression](#pdf-compression)
* [Amazon S3, Rackspace Cloud Files, and Google Cloud Storage](#amazon-s3-rackspace-cloud-files-and-google-cloud-storage)
    * [Amazon S3](#amazon-s3)
    * [Rackspace Cloud Files](#rackspace-cloud-files)
    * [Google Cloud Storage](#google-cloud-storage)

## Installation

    pip install krakenio

## Getting Started

First you need to sign-up for the [Kraken API](https://kraken.io/plans/) and obtain your unique **API Key** and **API Secret**. You will find both under [API Credentials](https://kraken.io/account/api-credentials). Once you have set up your account, you can start using Kraken.io's image optimization API in your applications.

## Downloading Images

Remember: never link to optimized images offered to download. You have to download them first, and then replace them in your websites or applications. Optimized images are available on our servers **for one hour** only, after which they are permanently deleted.

## How to use

You can optimize your images in two ways - by providing an URL of the image you want to optimize or by uploading an image file directly to Kraken API.

The first option (image URL) is great for images that are already in production or any other place on the Internet. The second one (direct upload) is ideal for your deployment process, build script or the on-the-fly processing of your user's uploads where you don't have the images available online yet.

## Wait and Callback URL

Kraken gives you two options for fetching optimization results. With the `wait` option set the results will be returned immediately in the response. With the `callback_url` option set the results will be posted to the URL specified in your request.

### Wait option

With the `wait` option turned on for every request to the API, the connection will be held open unil the image has been optimized. Once this is done you will get an immediate response with a JSON object containing your optimization results. To use this option simply set `"wait": true` in your request.

**Request:**

````js
{
    "auth": {
        "api_key": "your-api-key",
        "api_secret": "your-api-secret"
    },
    "url": "http://awesome-website.com/images/header.jpg",
    "wait": true
}
````

**Response**

````js
{
    "success": true,
    "file_name": "header.jpg",
    "original_size": 324520,
    "kraked_size": 165358,
    "saved_bytes": 159162,
    "kraked_url": "http://dl.kraken.io/d1aacd2a2280c2ffc7b4906a09f78f46/header.jpg"
}
````

### Callback URL

With the Callback URL the HTTPS connection will be terminated immediately and a unique `id` will be returned in the response body. After the optimization is over Kraken will POST a message to the `callback_url` specified in your request. The ID in the response will reflect the ID in the results posted to your Callback URL.

We recommend [hookbin](https://hookbin.com) as an easy way to capture optimization results for initial testing.

**Request:**

````js
{
    "auth": {
        "api_key": "your-api-key",
        "api_secret": "your-api-secret"
    },
    "url": "http://image-url.com/file.jpg",
    "callback_url": "http://awesome-website.com/kraken_results"
}
````

**Response:**

````js
{
    "id": "18fede37617a787649c3f60b9f1f280d"
}
````

**Results posted to the Callback URL:**

````js
{
    "id": "18fede37617a787649c3f60b9f1f280d"
    "success": true,
    "file_name": "file.jpg",
    "original_size": 324520,
    "kraked_size": 165358,
    "saved_bytes": 159162,
    "kraked_url": "http://dl.kraken.io/18fede37617a787649c3f60b9f1f280d/file.jpg"
}
````

## Authentication

The first step is to authenticate to Kraken API by providing your unique API Key and API Secret while creating a new Kraken instance:

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')
````

## Usage - Image URL

To optimize an image by providing image URL use the `kraken.url()` method. You will need to provide two mandatory parameters - `url` to the image and `wait` or `callback_url`:

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')

data = {
    'wait': True
}

result = api.url('your-image-url', data);

if result.get('success'):
    print result.get('kraked_url')
else:
    print result.get('message')
````

Depending on a choosen response option (Wait or Callback URL) in the `data` object you will find either the optimization ID or optimization results containing a `success` property, file name, original file size, kraked file size, amount of savings and optimized image URL:

````js
{
    success: true,
    file_name: 'file.jpg',
    original_size: 30664,
    kraked_size: 577,
    saved_bytes: 30087,
    kraked_url: 'http://dl.kraken.io/d1/aa/cd/2a2280c2ffc7b4906a09f78f46/file.jpg'
}
````

## Usage - Image Upload

If you want to upload your images directly to Kraken API use the `kraken.upload()` method. You will need to provide two mandatory parameters - `file` which is either a string containing a path to the file or a Stream Object and `wait` or `callback_url`.

In the `data` object you will find the same optimization properties as with `url` option above.

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')

data = {
    'wait': True
}

result = api.upload('/path/to/file.jpg', data);

if result.get('success'):
    print result.get('kraked_url')
else:
    print result.get('message')
````

## Usage - User status

If you want to check your quotas or your account status, you can use `user_status()` which will return a response similar to the following:


```json
{
    "success": true,
    "active": true,
    "plan_name": "Enterprise",
    "quota_total": 64424509440,
    "quota_used": 313271610,
    "quota_remaining": 64111237830
}
```

```python
from krakenio import Client

# Initialize Kraken client
api = Client(api_key="your-api-key", api_secret="your-api-secret")

# Get user status
result = api.user_status()

if result.get("success"):
    print("Success:", result)
else:
    print("Error:", result.get("message"))
```

## Lossy Optimization

When you decide to sacrifice just a small amount of image quality (usually unnoticeable to the human eye), you will be able to save up to 90% of the initial file weight. Lossy optimization will give you outstanding results with just a fraction of image quality loss.

To use lossy optimizations simply set `lossy: true` in your request:

````python
data = {
    'wait': True,
    'lossy': True
}
````

## Image Resizing

Image resizing option is great for creating thumbnails or preview images in your applications. Kraken will first resize the given image and then optimize it with its vast array of optimization algorithms. The `resize` option needs a few parameters to be passed like desired `width` and/or `height` and a mandatory `strategy` property. For example:

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')

data = {
    'wait': True,
    'lossy': True,
    'resize': {
        'width': 100,
        'height': 75,
        'strategy': 'crop'
    }
}

result = api.upload('/path/to/file.jpg', data);

if result.get('success'):
    print result.get('kraked_url')
else:
    print result.get('message')
````

The `strategy` property can have one of the following values:

- `exact` - Resize by exact width/height. No aspect ratio will be maintained.
- `portrait` - Exact width will be set, height will be adjusted according to aspect ratio.
- `landscape` - Exact height will be set, width will be adjusted according to aspect ratio.
- `auto` - The best strategy (portrait or landscape) will be selected for a given image according to aspect ratio.
- `crop` - This option will crop your image to the exact size you specify with no distortion.

## WebP Compression

WebP is a new image format introduced by Google in 2010 which supports both lossy and lossless compression. According to [Google](https://developers.google.com/speed/webp/), WebP lossless images are **26% smaller** in size compared to PNGs and WebP lossy images are **25-34% smaller** in size compared to JPEG images.

WebP's lossy compression:WebP compression no longer requires setting `'webp': True` . Instead, you should make a standard optimization request, and Kraken.io will handle WebP conversion based on your configured settings.

````python
data = {
    'wait': True,
    'lossy': True,
    'convert': {
        'format': 'webp'
    }
}
````

### Optimize WebP Image

```python
data = {
    'wait': True,
    'lossy': True
}
```

## PDF Compression

Kraken.io now supports PDF compression, allowing you to optimize PDF files with minimal loss of quality.

Kraken API automatically determines the optimal compression settings based on the content type of the PDF (e.g., image-heavy, text-heavy, or mixed content). Additionally, users can optionally provide custom parameters to further control the compression process.

```python
data = {
    'wait': True
}
```

**Optional Parameters:**

[API Docs for PDF Compression](https://kraken.io/docs/pdf-compression)

-   `level` - Optimization level for the PDF. Available options are `screen`, `ebook`, `printer` and `prepress`. **Overrides DPI values**.
-   `quality` - JPEG quality for embedded images. Acceptable values: **1-100**. Higher values preserve more detail but increase file size. Default is **65**.
-   `dpi` - Resolution for images within the PDF. Default value is calculated based on the PDF type. Adjust this value based on your desired output quality.
-   `downsampleType` - Method used to downsample images. Available options are `bicubic`, `average` and `subsample`


```python
data = {
    'wait': True,
    'level': 'ebook',
    'quality': 60,
    'dpi': 150,
    'downsampleType': 'bicubic'
}
```

## External Storage

Kraken API allows you to store optimized images directly in your S3, Cloud Files, Azure and SoftLayer. With just a few additional parameters your optimized images will be pushed to your external storage in no time.

### Amazon S3

**Mandatory Parameters:**
- `key` - Your unique Amazon "Access Key ID".
- `secret` - Your unique Amazon "Secret Access Key".
- `bucket` - Name of a destination container on your Amazon S3 account.
- `region` - Name of the region your S3 bucket is located in.

**Optional Parameters:**
- `path` - Destination path in your S3 bucket (e.g. `"images/layout/header.jpg"`). Defaults to root `"/"`.
- `acl` - Permissions of a destination object. This can be `"public_read"` or `"private"`. Defaults to `"public_read"`.

The above parameters must be passed in a `s3_store` object:

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')

data = {
    'wait': True,
    'lossy': True,
    's3_store': {
        'key': 'your-amazon-access-key',
        'secret': 'your-amazon-secret-key',
        'bucket': 'destination-bucket',
        'region': 'us-east-1'
    }
}

result = api.upload('/path/to/file.jpg', data);

if result.get('success'):
    print result.get('kraked_url')
else:
    print result.get('message')
````

The `result` object will contain `kraked_url` key pointing directly to the optimized file in your Amazon S3 account:

````js
{
    kraked_url: "http://s3.amazonaws.com/YOUR_CONTAINER/path/to/file.jpg"
}
````

### Rackspace Cloud Files

**Mandatory Parameters:**
- `user` - Your Rackspace username.
- `key` - Your unique Cloud Files API Key.
- `container` - Name of a destination container on your Cloud Files account.

**Optional Parameters:**
- `path` - Destination path in your container (e.g. `"images/layout/header.jpg"`). Defaults to root `"/"`.

The above parameters must be passed in a `cf_store` object:

````python
from krakenio import Client

api = Client('your-api-key', 'your-api-secret')

data = {
    'wait': True,
    'lossy': True,
    'cf_store': {
        'user': 'your-rackspace-username',
        'key': 'your-rackspace-api-key',
        'container': 'destination-container'
    }
}

result = api.upload('/path/to/file.jpg', data);

if result.get('success'):
    print result.get('kraked_url')
else:
    print result.get('message')
````

If your container is CDN-enabled, the optimization results will contain `kraked_url` which points directly to the optimized file location in your Cloud Files account, for example:

````js
kraked_url: "http://e9ffc04970a269a54eeb-cc00fdd2d4f11dffd931005c9e8de53a.r2.cf1.rackcdn.com/path/to/file.jpg"
````

If your container is not CDN-enabled `kraked_url` will point to the optimized image URL in the Kraken API:

````js
kraked_url: "http://dl.kraken.io/ec/df/a5/c55d5668b1b5fe9e420554c4ee/file.jpg"
````

### Google Cloud Storage

Kraken.io API allows you to store optimized images directly in your Google Cloud Storage (GCS) bucket. Follow the steps below to configure your GCS integration and securely store your optimized images.

#### Prerequisites:

Ensure you have access to Google Cloud Platform (GCP) and an active project where you will store your images.

#### Mandatory Parameters:

- `gcs_store.bucket` - Name of the destination bucket on your Google Cloud Storage account.
- `gcs_store.credentials` - Your service account credentials (JSON format) to authenticate with GCS.

#### Optional Parameters:

- `gcs_store.path` - Destination path in your GCS bucket (e.g., "images/layout/header.jpg"). Defaults to root `/`.
- `gcs_store.acl` - Permissions of the destination object. This can be "publicRead" or "private". Defaults to "private".
- `gcs_store.metadata` - Metadata you would like to assign to your GCS object (optimized image).

#### Important:

Make sure your Google Cloud Storage bucket has the appropriate permissions set to allow Kraken.io API to store images.

#### Step 1: Creating a Google Cloud Storage Bucket

1. Log in to your Google Cloud Console.
2. Navigate to the "Storage" section and select "Browser."
3. Click "Create bucket" and follow the prompts.
4. Note the bucket name for later use.

#### Step 2: Obtaining GCS Credentials

To interact with GCS through the API, you need appropriate credentials as a service account key:

1. Go to "IAM & Admin" in Google Cloud Console.
2. Select "Service Accounts" and click "Create Service Account."
3. Enter a name and description for the service account.
4. Assign necessary roles like "Storage Object Admin" or "Storage Object Creator."
5. Click "Create Key" and choose JSON type. This will download a JSON file with your credentials.
6. Securely store this JSON file. It contains sensitive information that allows access to your GCS resources.

#### Step 3: Configuring Your Kraken.io API Request

Include the necessary details in your Kraken.io API request to store the optimized image directly in your GCS bucket. Insert the JSON file's contents into the `credentials` property inside `gcs_store`.

```python
import json
import requests

from krakenio import Client

api = Client("your_api_key", "your_api_secret")

with open("path/to/your/credentials.json", "r") as f:
    credentials = json.load(f)

params = {
    "wait": True,
    "lossy": True,
    "gcs_store": {
        "acl": "private",
        "bucket": "your-bucket-name",
        "path": "path/to/your/image.png",
        "credentials": credentials
    }
}

result = api.url("https://example.com/image.png", params)

if result.get("success"):
    print(f"Success. Optimized image URL: {result.get('kraked_url')}")
else:
    print(f"Fail. Error message: {result.get('message')}")

```

## LICENSE - MIT

Copyright (c) 2025 Nekkra UG

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.