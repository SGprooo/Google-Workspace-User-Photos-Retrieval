# Google Workspace User Photos Retrieval

This repository contains Python scripts for retrieving user photos from a Google Workspace domain using the Directory API and the People API.

## Background

I initially tried to automate the download of profile images of all users under our Google Workspace domain to programmatically import their profiles into Odoo.

At first, I used the [Directory API](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users.photos/get) to retrieve user photos but it returned images with low resolution. To retrieve higher-resolution images, I switched to using the People API, but it resulted in the same limited photo resolution even after setting [image sizing parameters](https://developers.google.com/people/image-sizing).

I eventually found this [Google community post](https://support.google.com/mail/thread/11538455/how-can-i-view-someones-profile-picture-in-better-resolution?hl=en), so I instead scraped users using Beautiful Soup and modify the URL parameters to download high-res images in a separate project.

I thought of documenting this project incase someone may need to implement similar functionality.

## Set Up

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the [Directory API](https://console.cloud.google.com/apis/library/admin.googleapis.com) and [People API](https://console.cloud.google.com/apis/library/people.googleapis.com).
3. Create a service account and download the credentials JSON file.
4. Go to [Google Workspace Admin](https://admin.google.com/ac/owl/domainwidedelegation/) and enable Domain-wide Delegation for the service account, you will also need to enter the `client_id`, which can be found from the previously downloaded credentials JSON file.
5. Add the required scopes for the service account under Domain-wide Delegation in Google Workspace Admin:
    - For Directory API (used in `get_user_photo.py`): `https://www.googleapis.com/auth/admin.directory.user.readonly`
    - For People API (used in `get_user_photo_people.py`): `https://www.googleapis.com/auth/userinfo.profile`

## Scripts

### `get_user_photo.py` (Using Directory API)

This script uses the Directory API to retrieve user photos.

- Required OAuth Scopes:
    - `https://www.googleapis.com/auth/admin.directory.user.readonly`

### `get_user_photo_people.py` (Using People API)

This script uses the People API to retrieve user photos in higher resolution.

- Required OAuth Scopes:
    - `https://www.googleapis.com/auth/userinfo.profile`

## In regards to Impersonation

Initially, I faced a `403` error which indicated that the service account didn't have the necessary permissions without impersonation. 
The service account acts on its own and doesn't have permissions to access user data. By impersonating a user, especially an administrative one, it acts as if it's that user and can perform actions and access data that the impersonated user is permitted to. This is particulerly helpful in domain-wide scenarios where you want the service account to perform actions across different user accounts within your domain.