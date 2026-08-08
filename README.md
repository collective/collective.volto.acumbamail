# collective.volto.acumbamail

[![Latest Version](https://img.shields.io/pypi/v/collective.volto.acumbamail.svg)](https://pypi.org/project/collective.volto.acumbamail/) [![Supported - Python Versions](https://img.shields.io/pypi/pyversions/collective.volto.acumbamail.svg?style=plastic)](https://pypi.org/project/collective.volto.acumbamail/) [![Number of PyPI downloads](https://img.shields.io/pypi/dm/collective.volto.acumbamail.svg)](https://pypi.org/project/collective.volto.acumbamail/) [![License](https://img.shields.io/pypi/l/collective.volto.acumbamail.svg)](https://pypi.org/project/collective.volto.acumbamail/)

[![Acumbamail](https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/docs/source/_static/logo.svg)](https://acumbamail.com/)

An integration for the [Acumbamail](https://acumbamail.com/) service with Plone.

## Features

- Control panel in Plone registry to manage ``Acumbamail Settings``.

- RestApi endpoint that exposes the ``Acumbamail Settings`` for `Volto` _integration_.

- Add a [new subscriber](https://acumbamail.com/apidoc/function/batchAddSubscribers/) to the Acumbamail list.

## Screenshot

**Add-on Configuration Access**

<img width="290" alt="Add-on Configuration" src="https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/docs/source/images/addon-configuration-acumbamail-icon.png">

---

**Acumbamail Settings control panel**

<img width="720" alt="Acumbamail Settings" src="https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/docs/source/images/acumbamail-settings.png">

## Volto integration

To use this product in `Volto`, you needs to include the following add-on
in your project: [volto-acumbamail](https://github.com/collective/volto-acumbamail).

## Translations

This product support the following languages:

- Basque

- Catalan

- English

- Galician

- Spanish

## Compatibility

- Tested with `Python` 3.12 and {term}`Plone` 6.1.5.

## Install it

To install in your project, the `collective.volto.acumbamail` `add-on` with `pip` command:

```shell
pip install collective.volto.acumbamail
```

And to create the `Plone` site:

```shell
make create-site
```

## Custom REST services

### Acumbamail settings route

Anonymous users can't access registry resources by default with ``plone.restapi`` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi `route` with
``Acumbamail Settings`` (`@acumbamail-settings`):

Get the information from the ``Acumbamail Settings`` via `curl` command:

```shell
curl -X GET http://localhost:8080/Plone/@controlpanels/acumbamail-settings \
  -H "Accept: application/json" \
  --user admin:admin
```

This `route` returns a JSON object containing the ``Acumbamail`` settings and data via `curl` command:

```json
{
  "@id": "http://localhost:8080/Plone/@controlpanels/acumbamail-settings",
  "data": {
    "api_key": null,
    "api_url": null,
    "list_id": null
  },
  "group": "Add-on Configuration",
  "schema": {
    "fieldsets": [
      {
        "behavior": "plone",
        "description": "",
        "fields": [
          "api_url",
          "api_key",
          "list_id"
        ],
        "id": "general",
        "title": "General settings"
      }
    ],
    "properties": {
      "api_key": {
        "description": "Your Acumbamail personal token (https://acumbamail.com/api/)",
        "factory": "Text line (String)",
        "title": "API Key",
        "type": "string"
      },
      "api_url": {
        "description": "The URL of the Acumbamail API endpoint.",
        "factory": "Text line (String)",
        "title": "API URL",
        "type": "string"
      },
      "list_id": {
        "description": "Numeric identifier of the list where subscribers will be added.",
        "factory": "Text line (String)",
        "title": "List ID",
        "type": "string"
      }
    },
    "required": [
      "api_url",
      "api_key",
      "list_id"
    ],
    "type": "object"
  },
  "title": "Acumbamail Settings"
}
```

Below is a `PATCH` operation to set up the `api_url`, `api_key` and `list_id` fields values of the
``Acumbamail`` settings:

```shell
curl -i -X PATCH http://localhost:8080/Plone/@controlpanels/acumbamail-settings \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '{"api_url": "https://acumbamail.com/api/1", "api_key": "204615m3a78w2fgt3t1nm34567890123", "list_id": "4702726"}' \
  --user admin:admin
```

This `route` returns a HTTP response:

```shell
HTTP/1.1 204 No Content
Connection: close
Date: Sat, 25 Jul 2026 10:00:18 GMT
Server: waitress
Via: waitress
X-Powered-By: Zope (www.zope.dev), Python (www.python.org)
```

That means you updates the values in the ``Acumbamail Settings`` control panel fields correctly.

**NOTE:** You can validate the update operation, going to ``Site setup > Add-on Settings > Acumbamail Settings``.

---

### Acumbamail subscribe route

Anonymous users can't access registry resources by default with ``plone.restapi`` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi route called
`@acumbamail-subscribe`, below is a `POST` operation to add a new subscriber to the mailing list:

```shell
curl -i -X POST http://localhost:8080/Plone/@acumbamail-subscribe \
  -H "Accept: application/json" \
  -H "Accept-Language: es" \
  --data '{"email": "user@example.com"}' \
  --user admin:admin
```

This `route` can be used in for a _Volto integration_ form componet.

**NOTE:** You can validate the add operation, going to your ``Acumbamail`` Dashboard account.

## General resources

This part of the documentation contains reference material, including APIs, configuration values, and environment variables.

The Official API ``Acumbamail``

-   [Official API Acumbamail Documentation](https://acumbamail.com/apidoc/).

The ``Acumbamail`` endpoints that using:

-   The [batchAddSubscribers](https://acumbamail.com/apidoc/function/batchAddSubscribers/), is the Acumbamail endpoints that using.

## Contribute

- [Issue tracker](https://github.com/collective/volto-acumbamail/issues)
- [Source code](https://github.com/collective/volto-acumbamail/)
- [Documentation](https://collectivevoltoacumbamail.readthedocs.io/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.volto.acumbamail.git
    cd collective.volto.acumbamail
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

#### See also:

You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.

## Credits

Developed with the support of:

- [Instituto Municipal de Deportes - IMD, Seville City Council, Spain](https://imd.sevilla.org/).

  <img width="200" alt="IMD Logo" src="https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/docs/source/images/imd-ayto-logo.svg">

### Acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (eb40854)](https://github.com/plone/cookieplone-templates/commit/eb4085428af6261227bcb086ece110bbe5475d89) on 2025-11-06 19:48:38.313942. A special thanks to all contributors and supporters!

## Authors

This product was developed by [Leonardo J. Caballero G.](https://github.com/macagua).

<img width="100" alt="Leonardo J. Caballero G." src="https://avatars.githubusercontent.com/u/185395?v=4&size=100">

### Contributors

You can see a list of contributors in the [CONTRIBUTORS.md](https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/CONTRIBUTORS.md) file.

## License

The project is licensed under [GPLv2](https://raw.githubusercontent.com/collective/collective.volto.acumbamail/refs/heads/main/LICENSE.md).
