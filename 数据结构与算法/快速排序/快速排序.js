function swap(arr, i, j) {
   var tmp = arr[i];
   arr[i] = arr[j];
   arr[j] = tmp;
}

function quickSort(a, low, high){
	var left, right, pv;
	if (low >= high) return;
	
	pv = a[low];
	left = low;
	right = high;
	
	while(left != right) {
		while(a[right] >= pv && right > left)
			right--;
		while(a[left] <= pv && right > left)
			left++;
			
		if (right > left) {
			swap(a, left, right)
		}
	}
	
	// 基数的交换
	swap(a, low, left);
	
	quickSort(a, low, left-1);
	quickSort(a, left+1, high); 
}

arr = [1, 8, 5, 33, 2, 3, 5, 7]
quickSort(arr, 0, arr.length-1)
console.log(arr)
    
