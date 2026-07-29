---
myst:
  html_meta:
    "description": "Acumbamail integration with Plone Tutorials"
    "property=og:description": "Acumbamail integration with Plone Tutorials"
    "property=og:title": "Acumbamail integration with Plone Tutorials"
    "keywords": "Acumbamail, service, Plone, integration, documentation, tutorials"
---

# Custom REST services

{term}`Plone` can expose specific endpoints for {term}`Volto`. These services encapsulate
the logic for communicating with {term}`Acumbamail` and provide a standardised format
for the front end.

---

(acumbamail-settings-route)=
## @acumbamail-settings route

Anonymous users can't access registry resources by default with {term}`plone.restapi` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi route with {term}`Acumbamail Settings` (`@acumbamail-settings`):

Get the information from the {term}`Acumbamail Settings` via `curl` command:

```shell
curl -X GET http://localhost:8080/Plone/@controlpanels/acumbamail-settings \
  -H "Accept: application/json" \
  --user admin:admin
```

This route returns a JSON object containing the {term}`Acumbamail Settings` and data via `curl` command:

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

Below is a `PATCH` operation to set up the {term}`api_url`, {term}`api_key` and {term}`list_id` fields values of the
{term}`Acumbamail Settings`:

```shell
curl -i -X PATCH http://localhost:8080/Plone/@controlpanels/acumbamail-settings \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '{"api_url": "https://acumbamail.com/api/1", "api_key": "204615m3a78w2fgt3t1nm34567890123", "list_id": "4702726"}' \
  --user admin:admin
```

This route returns a HTTP response:

```shell
HTTP/1.1 204 No Content
Connection: close
Date: Sat, 25 Jul 2026 10:00:18 GMT
Server: waitress
Via: waitress
X-Powered-By: Zope (www.zope.dev), Python (www.python.org)
```

That means you were updated the values in the {term}`Acumbamail Settings` control panel fields correctly!

**NOTE:** You can validate the update operation, going to ``Site setup > Add-on Settings > Acumbamail Settings``.

---

(acumbamail-subscribe-route)=
## @acumbamail-subscribe route

Anonymous users can't access registry resources by default with {term}`plone.restapi` (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated RestApi route called
`@acumbamail-subscribe`, below is a `POST` operation to add a new subscriber to the mailing list:

```shell
curl -i -X POST http://localhost:8080/Plone/@acumbamail-subscribe \
  -H "Accept: application/json" \
  -H "Accept-Language: es" \
  --data '{"email": "user@example.com"}' \
  --user admin:admin
```

This `route` can be used in for a {term}`Volto` _integration_ form componet.

**NOTE:** You can validate the add operation, going to your {term}`Acumbamail` Dashboard account.
