def home(request): out=‘’
	if 'on' in request.POST:
		values = {"name": "on"}
		r=requests.put('http://127.0.0.1:8000/state/1/', data=values, auth=(‘username', ‘password')) result=r.text
		output = json.loads(result) out=output['name']
	if 'off' in request.POST:
		values = {"name": "off"}
		r=requests.put('http://127.0.0.1:8000/state/1/', data=values, auth=(‘username', ‘password')) result=r.text
		output = json.loads(result) out=output['name']
	if 'auto' in request.POST:
		values = {"name": "auto"}
		r=requests.put('http://127.0.0.1:8000/mode/1/', data=values, auth=(‘username', ‘password')) result=r.text
		output = json.loads(result) out=output['name']
	if 'manual' in request.POST:
		values = {"name": "manual"}
		r=requests.put('http://127.0.0.1:8000/mode/1/', data=values, auth=(‘username', ‘password')) result=r.text
		output = json.loads(result) out=output['name']
	r=requests.get('http://127.0.0.1:8000/mode/1/', auth=(‘username', ‘password')) 
	result=r.text
	output = json.loads(result) 
	currentmode=output['name']
	r=requests.get('http://127.0.0.1:8000/state/1/', auth=(‘username', ‘password')) 
	result=r.text
	output = json.loads(result) 
	currentstate=output['name']
	return render_to_response('lights.html',{'r':out, 'currentmode':currentmode, 'currentstate':currentstate}, 
context_instance=RequestContext(request))