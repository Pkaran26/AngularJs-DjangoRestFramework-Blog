app.controller('read', function($scope, $http, $stateParams){
    if ($stateParams.id){
        $scope.id = $stateParams.id;
        $http.get('http://localhost:8000/blog/v1/post/'+$scope.id+"/").then(function(res){
            $scope.read = res.data;
            //console.log($scope.read);
        });
    }else{
        $state.go("home");
    }
});