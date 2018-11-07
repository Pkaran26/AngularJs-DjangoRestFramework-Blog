app.config(function ($stateProvider, $urlRouterProvider){
    $stateProvider.state("home", {
        url: "/home",
        templateUrl: "templates/home.html",
        controller: "home"
    })
    .state("read", {
        url: "/read/:id",
        templateUrl: "templates/read.html",
        controller: "read"
    });
    $urlRouterProvider.otherwise("/home");
});