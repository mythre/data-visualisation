var data = {
            data1: [30, 20, 50, 40, 60, 50],
            data2: [200, 130, 90, 240, 130, 220],
            data3: [300, 200, 160, 400, 250, 250]
        };

function display_chart(data) {
    console.log('Displaying chart' + data)
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            // json:{
            //     data
            // }
          columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 50, 20, 10, 40, 15, 25]
          ]
        }
    });
};


$(document).ready(function() {
    $('#btn').click(function(){
        display_chart(data);
    });
    // setInterval(update, 1000);
});


function update() {
    $.ajax({
  url: "",
  // data: {
  //   zipcode: 97201
  // },
  success: function( result ) {
    display_chart(data)
  }
});
};
