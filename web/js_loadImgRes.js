// 单张图片(图片动态生成)
var xiu = new Image();
xiu.src = 'http://www.daqianduan.com/wp-content/uploads/2014/11/hs-xiu.jpg';
xiu.onload = function(){
	//加载完成
}

//单张图片（结合ES6 Promise）
new Promise((resolve, reject)=>{
	let xiu = new Image()
	xiu.src = 'http://www.daqianduan.com/wp-content/uploads/2014/11/hs-xiu.jpg'
	xiu.onload = function(){
   		// 加载完成 
   		resolve(xiu)
	}
	}).then((xiu)=>{
//code
})



// 用来加载网页所需的图片资源
var img = [],
flag = 0,
mulitImg = [
	'http://www.daqianduan.com/wp-content/uploads/2017/03/IMG_0119.jpg',
	'http://www.daqianduan.com/wp-content/uploads/2017/01/1.jpg',
    'http://www.daqianduan.com/wp-content/uploads/2015/11/jquery.jpg',
    'http://www.daqianduan.com/wp-content/uploads/2015/10/maid.jpg'
];

var imgTotal = mulitImg.length;
for (var i = imgTotal - 1; i >= 0; i--) {
	img[i] = new Image();
	img[i].src = mulitImg[i];
	img[i].onload = function(){

		flag++;

		if (flag == imgTotal) {
			console.log("全部加载完成...");

			setTimeout(function(){
				$("#id_img_1").attr('src',img[2].src); 
			}, 5000);
		}
	}
}


// 多张图片（结合ES6 Promise.all()）
let mulitImg = [
     'http://www.daqianduan.com/wp-content/uploads/2017/03/IMG_0119.jpg',
     'http://www.daqianduan.com/wp-content/uploads/2017/01/1.jpg',
     'http://www.daqianduan.com/wp-content/uploads/2015/11/jquery.jpg',
     'http://www.daqianduan.com/wp-content/uploads/2015/10/maid.jpg'
 ];
 let promiseAll = [], img = [], imgTotal = mulitImg.length;
 for(let i = 0 ; i < imgTotal ; i++){
     promiseAll[i] = new Promise((resolve, reject)=>{
         img[i] = new Image()
         img[i].src = mulitImg[i]
         img[i].onload = function(){
              //第i张加载完成
              resolve(img[i])
         }
     })
 }
 Promise.all(promiseAll).then((img)=>{
 	console.log("全部加载完成");
     //全部加载完成
	$("#id_img_1").attr('src',img[2].src); 
 })