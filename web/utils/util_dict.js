// 工具类
var util_dic = {
  isEmptyObject: function (obj){
    if (JSON.stringify(obj) == '{}') {
        return true;
    } else {
        return false;
    }
  }
}