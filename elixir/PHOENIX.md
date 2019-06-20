Notes to self about how Elixir/Phoenix or just templating works:

Phoenix by default structures an app like:
`lib/appname_web/templates/layout` contains the enclosing html header, nav, etc.
`lib/appname_web/templates/pages` contains the sub-templates of a site, like for blog posts