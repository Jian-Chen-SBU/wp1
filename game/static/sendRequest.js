grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
gameEnded = false;
$(document).ready(function(){
    
    $("#table td").click(function() {
        if(!gameEnded) {
            var index = 0;
            var row = parseInt( $(this).parent().index() )+1; 
            var col = parseInt( $(this).index() ) + 1;
            if(row == 1) {
                index = col - 1;
            } else if(row == 2) {
                index = 3 + col - 1;
            } else {
                index = 6 + col - 1;
            }
            grid[index] = "X";
            $("#" + index).text("X");        
            send_request();
        }
    });
});

function send_request() {
	grid_data = {"grid" : grid};
    if(!gameEnded) {
        $.ajax({        
            method: 'POST',
            url: '/ttt/play',              
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(grid_data),        
            success: function(data){
                grid = data['grid'];
                for(let i = 0; i < 9; i++) {
                    $("#" + i).text(grid[i]);
                }            
                if(data['winner'] != undefined) {
                    winner = data['winner'];
                     if(winner == "X" || winner == "O") {
                        $("#winner").text("The winner is: " + winner);
                        gameEnded = true;
                    } 
                }                                
            }              
        });
    }	
}
