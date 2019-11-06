let levels = []
let relation = []
$.get('/levels.json', function(data){
	levels = [data.levels]
})
$.get('/relation.json', function(data){
	relation = [data.relations]
})