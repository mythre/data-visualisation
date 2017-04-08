// var data = {
//             data1: [30, 20, 50, 40, 60, 50],
//             data2: [200, 130, 90, 240, 130, 220],
//             data3: [300, 200, 160, 400, 250, 250]
//         };

function display_chart(data) {
    // console.log('data: ' + data)
    // console.log('data[data]: ' + data['data'])
    var chart = c3.generate({
        bindto: '#chart',
        data: {
            json:data['data'],
            keys:{
              value: ['count'],
              x: data['key']
            },
            type: 'bar',
            x: 'x'
          // columns: [
          //   ['data1', 30, 200, 100, 400, 150, 250],
          //   ['data2', 50, 20, 10, 40, 15, 25]
          // ]
        },
        axis: {
          x: {
              type: 'category' // this needed to load string x value
          }
        },
        bar: {
            width: {
                ratio: 0.5 // this makes bar width 50% of length between ticks
            }
            // or
            //width: 100 // this makes bar width 100px
        }
    });
};


$(document).ready(function() {
    $('#btn').click(function(){
        update();
    });
    

    // update_mar();
    // display_chart(data);
    setInterval(update_mar, 20000);
    setTimeout(setInterval(update_ind, 20000), 10000);
});


function update_mar() {
    $.ajax({
  url: "/marital_data/",
  // data: {
  //   zipcode: 97201
  // },
  success: function( result ) {
    // $('#response').text(result)
    display_chart(result)
  }
});
};

function update_ind() {
    $.ajax({
  url: "/industry_data/",
  // data: {
  //   zipcode: 97201
  // },
  success: function( result ) {
    // $('#response').text(result)
    display_chart(result)
  }
});
};
