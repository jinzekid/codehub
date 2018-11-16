// 堆排序：js版本	
function ClsHeapSort() {

	this.sort = function(L, size) {
		var n = size;
		while (n > 0) 
		{
			swap(L, 0, n-1);
			n -= 1;
			sift_down(L, 0, n);
		}
	}
		
	this.build = function(L, size) {
		var n = size;
		var firstPIdx = parseInt(n/2)-1
		for (var i = firstPIdx; i >= 0 ;i--) {
			sift_down(L, i, n);
		}
	}
	
	this.insert = function(L, data) {
		L.push(data)
		sift_up(L, L.length)
	}

	function swap(L, a, b) {
		var t = L[a]
		L[a] = L[b]
		L[b] = t
	}
	
	function sift_down(L, idx, size) {
		var n = size;
		var t_pos;
		var i = idx;
		var flag = 0;
		
		// 注意取整问题：parseInt(n/2)
		while(i < (parseInt(n/2)) && flag == 0) {
			if (L[i] > L[2*i+1])
				t_pos = 2*i+1;
			else 
				t_pos = i;
				
			if (2*i+2 < n && L[t_pos] > L[2*i+2]) {
				t_pos = 2*i+2;
			}
			
			if (i != t_pos) {
				swap(L, t_pos, i)
				i = t_pos;
			}
			else {
				flag = 1;
			}
		}
	}
	
	function sift_up(L, size) {
		var n = size;
		var i = n-1;
		var flag = 0;
		while (i >= 0 && flag == 0) {
			// 注意取整问题：parseInt(i/2)
			var parent_idx = parseInt(i/2)
			console.log("parent_idx==="+parent_idx);
			if (L[i] > L[parent_idx]) {
				swap(L, i, parent_idx);
				i = parent_idx;
				console.log("i==="+i);
			}
			else {
				flag = 1
			}
		}
	}
	
}



var list = [22,1,32,324,2]
var heap = new ClsHeapSort(list)

heap.build(list, list.length)
console.log("-----before sort-----")
console.log(list)

console.log("-----after sort-----")
heap.sort(list, list.length)
console.log(list)

console.log("-----insert '30' data-----")
heap.insert(list, 30)
console.log(list)

console.log("-----rebuild heap-----")
heap.build(list, list.length)
console.log(list)

console.log("-----after sort-----")
heap.sort(list, list.length)
console.log(list)


