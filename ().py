# coding: utf-8
from posts.models import Author, Post

author1 = Author(nick = 'testowy', email = 'jakis@exapmle.com', bio = 'cos o autorze')
author2 = Author(nick = 'testow3y', email = 'jaki634ds@exapmle.com', bio = 'cos o autorze')
author3 = Author(nick = 'testow4y', email = 'jaki24s@exapmle.com')
author4 = Author(nick = 'testow5y', email = 'jak134ds@exapmle.com', bio = 'cos o autorze')
author5 = Author(nick = 'testow6y', email = 'jak324ds@exapmle.com')
author6 = Author(nick = 'testow7y', email = 'jakfsdfsds@exapmle.com', bio = 'cos o autorze')
get_ipython().run_line_magic('save', '()')
