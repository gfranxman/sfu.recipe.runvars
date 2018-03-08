Introduction
************

This recipe can be used to populate a buildout part with variables
whose values come from external commands.

.. contents::

A short example::


  [sekrets]
  recipe = sfu.recipe.runvars
  username = somedewd
  password = `lpass show --password somedewd@some.api.com`

Now you are free to use ${sekrets:username} and ${sekrets.password} in
other parts or templates as part of your buildout.

This is useful for populating environment variables as part of system
configuration, for example.

