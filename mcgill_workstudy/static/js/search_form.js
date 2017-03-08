/**
 * Created by aarongaba on 2017-03-06.
 */

var academicTerms = /(Fall|Spring|Summer|Winter) (\d{4})/g;

var app = angular.module('searchForm', []);

app.controller('formController', function($scope) {
    $scope.selectedSeason = "";
    $scope.selectedYear = "";

    $scope.setTermInfo = function(){
        console.log($scope.selectedTerm);
        var match = academicTerms.exec($scope.selectedTerm);
        console.log(match);
        if (match) {
            $scope.selectedSeason = match[1];
            $scope.selectedYear = match[2];
        }
    }
});
