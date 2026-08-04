---
myst:
  html_meta:
    "description": "Acumbamail integration with Plone how-to guides"
    "property=og:description": "Acumbamail Plone how-to guides"
    "property=og:title": "Acumbamail integration with Plone how-to guides"
    "keywords": "Acumbamail, service, Plone, integration, documentation, how-to, guides"
---

# Security access

The {term}`collective.volto.acumbamail` {term}`add-on` includes the following roles and permissions:

## Roles

- ``Acumbamail`` role.

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

## Permissions

- ``volto.acumbamail: Manage Acumbamail Settings``

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

  This permission grants access to the following roles:

  - ``Acumbamail`` role.

    ```{tip}
    If to grant this role to a user, this inherited the permissions that included, and there are details bellow:
    ```

- The ``Plone Site Setup: Overview`` permission grants access to the `Site Setup: Overview ` view to the following roles:

  - The ``Manager`` role.

  - The ``Site Administrator`` role.

  - The ``Acumbamail`` role.
