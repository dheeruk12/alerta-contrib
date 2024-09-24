Zenduty Plugin
================

**Tip: Use this plugin in conjunciton with the Alerta webhook which will notify
Zenduty when a Alerta will create or update the alerts.**

Installation
------------

To install remotely from GitHub run:
### Step 1: In Alerta-Api bash
```python
pip install git+https://github.com/Zenduty/alerta-contrib.git#subdirectory=plugins/zenduty
```
### Step 2: In Alerta-Web bash
```python
/venv/bin/pip install git+https://github.com/Zenduty/alerta-contrib.git#subdirectory=plugins/zenduty
```

Note: If Alerta is installed in a python virtual environment then plugins
need to be installed into the same environment for Alerta to dynamically
discover them.

Configuration
-------------

Add `zenduty` to the list of enabled `PLUGINS` in `alertad.conf` server
configuration file and set plugin-specific variables either in the
server configuration file or as environment variables.

DASHBOARD_ID = Tenant ID from zenduty account connection

```python
PLUGINS=zenduty
DASHBOARD_ID = ''
```

**Example**

```python
PLUGINS=reject,heartbeat,blackout,zenduty
DASHBOARD_ID=d9f75dbb0b5643268a993159207b98a1
```

References
----------

  * Zenduty Integration Docs: (https://www.zenduty.com/docs/alerta-integration/)

