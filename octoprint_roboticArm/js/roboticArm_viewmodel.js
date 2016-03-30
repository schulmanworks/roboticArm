$(function() {
    function roboticArm_viewmodel(parameters) {
        var self = this;

        self.loginState = parameters[0]; // requested as first constructor parameter below

        // more of your viewmodel's implementation
    }

    OCTOPRINT_VIEWMODELS.push([
        roboticArm_viewmodel,
        ["controlViewModel"],
        ["#roboticArm"]
    ]);
})
