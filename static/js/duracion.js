
var myApp = angular.module("MyApp", [])
myApp.controller('testCtrl', ['$scope',
  function($scope) {
    $scope.duration = 90;
    $scope.timeDuration = {
      minutes: 2,
      seconds: 50
    };
  }
]);
myApp.directive('durationInput', function() {
  return {
    restrict: 'A',    
    scope: {},
    require: 'ngModel',
    link: function(scope, element, attrs, ngModelCtrl) {
      getDisplayValue = function(value){
        var duration =  moment.duration(value, 'seconds');  
        minutes =  duration.minutes();
        seconds =  duration.seconds();
        if(minutes < 10){
          minutes = "0" + minutes
        }
        if(seconds < 10){
          seconds = "0" + seconds
        }
        return minutes + ":" + seconds;
      }
      ngModelCtrl.$formatters.push(function (value) {    
        return getDisplayValue(value);
      });
      ngModelCtrl.$parsers.push(function(value){
        if(value.indexOf(":") == -1){
          value = "00:" + value;
        }
        val = moment.duration("00:" + value).asSeconds();  
        return val;
      }); 
      setViewValue = function(){
        ngModelCtrl.$setViewValue(element[0].value);
        element[0].value = getDisplayValue(ngModelCtrl.$modelValue);
      }
      element.on('blur',setViewValue);
    }
  }
});
myApp.directive('timeDurationInput', function() {
  var tpl = '<div class="duration_input"> \
	          <input ng-model="duration.minutes" type="number" class="minutes" placeholder="00" min="0" max="60" step="1"> \
            <span class="duration-sep">:</span> \
            <input ng-model="duration.seconds" type="number" class="seconds" placeholder="00" min="5" max="59" step="1"> \
            </div>';

  return {
    restrict: 'A',
    template: tpl,
    scope: {},
    require: 'ngModel',
    link: function(scope, element, attrs, ngModelCtrl) {      
      ngModelCtrl.$render = function() {        
        scope.duration = ngModelCtrl.$viewValue
      }
      scope.$watch('duration', function(val) {        
        ngModelCtrl.$setViewValue(scope.duration);
      });      
    }
  }
});