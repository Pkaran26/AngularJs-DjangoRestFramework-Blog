app.controller('search', function($scope, $http, $stateParams){

        $scope.getPost = function(url){
            $http.get(url).then(function(res){
                $scope.searchdata = res.data.results;
                $scope.snext = res.data.next;
                $scope.sprevious = res.data.previous;
            });
        }
    //$state
        $scope.readPost = function(id){
            $state.go("read", {"id": id});
        }
        
        $scope.snextPage = function(){
            $scope.getPost($scope.snext);
        }
    
        $scope.sprevPage = function(){
            $scope.getPost($scope.sprevious);
        }
        if ($stateParams.id){
            $scope.id = $stateParams.id;
            $scope.getPost('http://localhost:8000/blog/v1/post/search/'+$scope.id+"/");
        }else{
            $state.go("home");
        }
});