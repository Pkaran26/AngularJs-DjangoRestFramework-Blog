var app = angular.module('app', ["ui.router"]);
var cate = [];
var user = [];
var cate_count = 0;
var user_count = 0;

app.filter("getCategory",function () {
    return function (id) {
        for(var i = 0; i < cate_count; i++) {
            if(cate[i].id==id){
                return cate[i].category;
            }
        }
    };
});

app.filter("getUser",function () {
    return function (id) {
        for(var i = 0; i < user_count; i++) {
            if(user[i].id==id){
                return user[i].username;
            }
        }
    };
});