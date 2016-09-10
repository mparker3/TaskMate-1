$(document).ready(function(){
    $('#datepicker').datepicker({
        orientation: "bottom",
        dateFormat: 'mm-dd-yyyy',
        startDate: "09/10/2016"
        
    });
    $("#submit").click(function() {
        selecteddate = $('#datepicker').datepicker('getDate');
        task = $("#task").val();
        hours = $("#duration_hours").val();
        minutes = $("#duration_minutes").val();
        if (task == null || task == "" || selecteddate == null || selecteddate == "" || hours == null || hours == "" || hours > 12 || minutes == null || minutes == "" || minutes > 59) {
            if (hours > 12 || minutes > 59){
                alert("Task cannot be over 12 hours or over 59 minutes");
                return false;
            }
            else {
                alert("Please fill out all fields");
                return false;
            }
        }
        duration = (hours*60) + parseInt(minutes);
        if ($("#importance").val() == "Medium Importance"){
            importance = 2
        }
        else if ($("#importance").val() == "Low Importance"){
            importance = 1
        }
        else {
            importance = 3
        }
        deadline = (selecteddate.getMonth()+1) + "/" + selecteddate.getDate() + "/" + selecteddate.getFullYear();
        
        var sendtask = {
            task_desc: task,
            task_duration: duration,
            task_importance: importance,
            task_deadline: deadline
        };
        
        console.log(sendtask);
        var JSONtask = JSON.stringify(sendtask);
        
    });
});

