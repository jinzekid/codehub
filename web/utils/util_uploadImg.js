// 工具类
var upload_img = {

  /*************************************************图片类工具*************************************************/
  // 初始化：多个文件上传 属性
  init_upload_file_btn: function(jq_file_btn, list_cur_files) {
    //选择文件按钮
    var $file = $(jq_file_btn)
      /*
      选择按钮change事件，实例化fileReader,调它的readAsDataURL并把原生File对象传给它，
      监听它的onload事件，load完读取的结果就在它的result属性里了。
      它是一个base64格式的，可直接赋值给一个img的src.
      */
      $file.on('change',function(){       
      //原生的文件对象，相当于$file.get(0).files[0];
      console.log(this.value);
      curFile = this.files;

      var file_names = "";
      for(var i=0,len = list_cur_files.length;i < len;i++){
        file_names += list_cur_files[0].name;
      }

      //var sign = hex_md5(file_names)
      //console.log("file name:" + file_names +", sign:" + sign);

      //将FileList对象变成数组
      list_cur_files = list_cur_files.concat(Array.from(curFile));
      $list = $(jq_list);
      for(var i=0,len = curFile.length;i < len;i++){
        util.reviewFile(curFile[i])
      }
    })

    // function reviewFile(file){
    //   //实例化fileReader,
    //   let  fd = new FileReader();
    //   //获取当前选择文件的类型
    //   let fileType = file.type;
    //   //调它的readAsDataURL并把原生File对象传给它，
    //   // fd.readAsDataURL(file);//base64
    //   //监听它的onload事件，load完读取的结果就在它的result属性里了
      
    //   fd.onload = function(){
    //     var sign = hex_md5(file.name + file.size)
    //     console.log("file name:" + file.name +", sign:" + sign);

    //     if(/^image\/[jpeg|png|jpg|gif]/.test(fileType)){
    //       $list.append('<li class="file-item" style="border-bottom: 1px solid #c0c0c0;padding-bottom: 10px;"><img style="width: 40px;" src="'+this.result+'" alt=""><span class="file-name">'+file.name+'</span><span id="id_span_file_status_'+sign+'" class="file-del" style="float: right;">'+loginFns.data.file_status.DEL+'</span></li>')
    //     }else{
    //       $list.append('<li class="file-item" style="border-bottom: 1px solid #c0c0c0;padding-bottom: 10px;"><img style="width: 40px" src="./img/ic_file_video.png"><span class="file-name">'+file.name+'</span><span id="id_span_file_status_'+sign+'" class="file-del" style="float: right;">'+loginFns.data.file_status.DEL+'</span></li>')
    //     }
    //     checkFileLen();
    //   }
    //   console.log(file);
    //   fd.readAsDataURL(file); 
    // }

    // 检查长度，来现实上传按钮
    function checkFileLen() {
    var jq_a = "#id_upload_a_"+loginFns.data.line_id_multiple_upload;
      if ($list.is(':empty')) {
        $(jq_a).hide();
      }
      else {
        $(jq_a).show();
      }
    }

   // 删除按钮事件
   $(jq_list).on('click','.file-del',function(){
       let $parent = $(this).parent();
       let index = $parent.index();
       loginFns.data.fileList.splice(index,1);
       $parent.remove()

       checkFileLen()
   });
  },
  // 预览图片
  reviewFile: function(file, $list){
    //实例化fileReader,
    let  fd = new FileReader();
    //获取当前选择文件的类型
    let fileType = file.type;
    //调它的readAsDataURL并把原生File对象传给它，
    fd.readAsDataURL(file);//base64
    //监听它的onload事件，load完读取的结果就在它的result属性里了

    fd.onload = function(){
      console.log("初始化图片结束...")
      // if(/^image\/[jpeg|png|jpg|gif]/.test(fileType)){
      //    $list.append('<li class="file-item"><img src="'+this.result+'" alt=""><span class="file-name">'+file.name+'</span><span class="file-del">删除</span></li>')
      // }else{
      //    $list.append('<li class="file-item"><span class="file-name">'+file.name+'</span><span class="file-del">删除</span></li>')
      // }
    }

    /*
    var jq_a = "#id_upload_a_"+loginFns.data.line_id_multiple_upload;
    if ($list.length > 0) {
      $(jq_a).show();
    }
    else {
      $(jq_a).hide();
    }
    */
  },
  // 判断是否是图片后缀
	is_img_url:function(url) {
    var arr = url.split('.')
    var type = arr[arr.length-1]
    var low_format = type.toLowerCase()
    if(low_format == "jpg" || low_format == "png" || low_format == "gif" || low_format == "jpeg"){
      return true;
    }

    return false;
  },
  // 获取图片缓存
  get_image_width: function(url,callback){
    var img = new Image();
    img.src = url;

    // 如果图片被缓存，则直接返回缓存数据
    if(img.complete){
        callback(img.width, img.height);
    }else{
            // 完全加载完毕的事件
      img.onload = function(){
        callback(img.width, img.height);
      }
    }
  },
  // 根据分隔符，分割字符串
  split_str:function(str_org, str_split) {
    var a = str_org.split(str_split);
    return a;
  },
  // 获取日期xxxx-xx-xx dd-dd中的xxxx-xx-xx
  get_date_yymmdd: function(str_date) {
    var a = str_date.split(" ");
    return a[0];
  },
  del_element: function(arr, element) {
    var delName= element;
    for(var i=0;i<arr.length;i++)
    {
      var nameTemp = arr[i];
      if(nameTemp===delName)
        {
        arr.splice(i,1);
      }
    }
  }
}