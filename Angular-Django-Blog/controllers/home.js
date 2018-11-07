app.controller('home', function($scope, $http, $state){
    $scope.getPost = function(url){
        $http.get(url).then(function(res){
            $scope.post = res.data.results
            $scope.next = res.data.next;
            $scope.previous = res.data.previous;
            //console.log(res.data.previous);
        });
    }
//$state
    $scope.readPost = function(id){
        $state.go("read", {"id": id});
    }

    $scope.categoryList = function(){
        $http.get('http://localhost:8000/blog/v1/category/').then(function(res){
            $scope.category = res.data
            cate = angular.fromJson(res.data);
            cate_count = res.data.length;
        });
        $http.get('http://localhost:8000/blog/v1/post/user/').then(function(res){
            user = angular.fromJson(res.data);
            user_count = res.data.length;
        });
    }
    
    $scope.nextPage = function(){
        $scope.getPost($scope.next);
    }

    $scope.prevPage = function(){
        $scope.getPost($scope.previous);
    }

    $scope.categoryList();
    $scope.getPost('http://localhost:8000/blog/v1/post/');
    
});
