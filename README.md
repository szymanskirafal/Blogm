**Blogm is simple blog application.**</br>

User can write articles or antries and add comments.

The app is created with Django Rest Framework in a docker container.

**User can register using this path**

/api/dj-rest-auth/registration/

**Login / log out and other functionalities are here:**

/api/dj-rest-auth/login/

/api/dj-rest-auth/logout/

/api/dj-rest-auth/password/reset/

/api/dj-rest-auth/password/reset/confirm/


**There's facebook login option**

/api/dj-rest-auth/facebook/


**Blog functionalities are:**

/api/articles/ - where user can see the list of all articels, a specific article or create new one

/api/entries/ - where user can see the list of all entries, a specific entry or create new one

/api/comments/ - where user can see the list of all comments, a specific comment or create new one

/api/comments/?asset_category=article&asset_pk=1 - where user can see the list of comments for given asset

