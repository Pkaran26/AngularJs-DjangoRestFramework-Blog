app.controller('read', function($scope, $http, $stateParams){
    if ($stateParams.id){
        $scope.id = $stateParams.id;
        $http.get('http://localhost:8000/blog/v1/post/'+$scope.id+"/").then(function(res){
            $scope.post = res.data;
            console.log($scope.post);
        });
    }
});