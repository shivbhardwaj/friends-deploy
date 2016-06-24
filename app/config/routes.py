from system.core.router import routes

routes['default_controller'] = 'Friends'
routes['GET']['/']= 'Friends#index'
routes['GET']['/friend/<id>']='Friends#show'
routes['GET']['/friend/new']="Friends#add"
routes['GET']['/friend/<id>/edit']="Friends#update"
routes['GET']['/friend/<id>/delete/process']='Friends#delete_process'
routes['GET']['/friend/<id>/delete']='Friends#delete'
routes['POST']['/friend/<id>/update/process']='Friends#update_process'
routes['POST']['/friend/new/process']='Friends#add_process'