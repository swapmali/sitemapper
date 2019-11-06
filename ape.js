let levels_1 = [
	['http://cse.nitk.ac.in'],
	['sites', 'courses'],
	['default', 'doctoral', 'pg'],
	['files'],
	['uploads'],
	['IoTfinal-brochure_0.pdf','SUC%2719-Brochure.pdf','cybersecuritysecond.pdf']
];
let relation_1 = [
	[['sites', 'courses'], [], [], [], [], []],
	[['default'], ['doctoral', 'pg'], [], [], [], []],
	[['files'], [], [], [], [], []],
	[['uploads'], [], [], [], [], []],
	[['IoTfinal-brochure_0.pdf','SUC%2719-Brochure.pdf','cybersecuritysecond.pdf'],
		[],[],[],[],[]
	],
	[[], [], [], [], [], []]
];

// function buildChildren(i, j){
// 	for (; i < levels_1.length; i++) {
// 		for (; j < levels_1[i].length; j++) {
// 			let y = {}
// 			let x = []
// 			if(relation_1[i][j].length){
// 				for(let k = 0; k < relation_1.length; k++) {
// 					x.push({
// 						name: relation_1[i][j],
// 						children: buildChildren(i+1, k)
// 					})
// 				}
// 			}
// 			else x.push({
// 				name: levels_1[i][j],
// 				children: []
// 			})
// 			y.name = levels_1[i][j]
// 			y.children = x;
// 			return y
// 		}
// 	}
// }

/*-----------------working version 1---------------*/
function buildChildren(i, j){
	for (; i < levels_1.length; i++) {
		let x = []
		for (; j < levels_1[i].length; j++) {
			if(relation_1[i][j].length){
				if(x.length <= relation_1[i][j].length){
					x.push({
						name: levels_1[i][j],
						children: buildChildren(i+1, j)
					})
				}
			}
			else x.push({
				name: levels_1[i][j],
				children: []
			})
		}
		return x
	}
}


console.log('build children',buildChildren(0,0));

function getChildren(arr) {
	return arr.reduce((acc, cur) => {
		return [...acc, { name: cur, children: [] }];
	}, []);
}

let children = []
let children_obj = {}

for(let i = 0; i < levels_1.length; i++) {
	for(let j = 0; j < levels_1[i].length; j++) {
		if(relation_1[i][j].length){
			let x = getChildren(relation_1[i][j]);
			let name = levels_1[i][j];
			let y = {
				name,
				children: x
			}
			children.push(y)
			children_obj[name] = x
		}
	}
}
console.log(children)
console.log(children_obj)
/*
	let treeData = {
		name: 'Top Level',
		children: [
			{
				name: 'Level 2: A',
				children: [{ name: 'Son of A' }, { name: 'Daughter of A' }]
			},
			{ name: 'Level 2: B' }
		]
	};
*/
let treedata = {
	name: levels_1[0][0],
	children: children_obj[levels_1[0][0]]
}

treedata.children.forEach(child => {
	child.children = addChildren(child.name)
});

function addChildren(name) {
	if(children_obj.hasOwnProperty(name))
		return children_obj[name]
	else return []
}

// console.log(treedata)



// for (let i = 0; i < levels_1.length; i++) {
// 	let level = levels[i]
// 	for (let j = 0; j < level.length; j++) {
// 		for(let k = 0; k < relation_1[j][k].length; k++){
// 			if(relation[j][k].length) {
// 				let x = getChildren(relation[j][k])
// 				let y = {
// 					name: level[j],
// 					children: x
// 				}
// 				children.push(y);
// 			}
// 		}
// 	}
// }


/*
let treeData = {
	name: 'http://cse.nitk.ac.in',
	children: [
		{
			name: 'sites',children: []
		},
		{
			name: 'courses',children: [] 
		}
	] 
}
*/
