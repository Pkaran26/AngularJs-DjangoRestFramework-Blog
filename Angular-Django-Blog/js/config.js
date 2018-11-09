app.config(function ($stateProvider, $urlRouterProvider){
    $stateProvider.state("home", {
        url: "/home",
        params: {
            id: null,
          },
        templateUrl: "templates/home.html",
        controller: "home"
    })
    .state("read", {
        url: "/read/:id",
        templateUrl: "templates/read.html",
        controller: "read"
    })
    .state("search", {
        url: "/search/:id/:type",
        templateUrl: "templates/search.html",
        controller: "search"
    });
    $urlRouterProvider.otherwise("/home");
});