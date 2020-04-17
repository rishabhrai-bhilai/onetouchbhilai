if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
  } else {
    ready()
  }
  function ready() {

    gettingTotal();
    myFunction();

    var gets = document.getElementsByClassName('radio');
    for (var i = 0; i < gets.length; i++)
     {
        var button = gets[i]
        button.addEventListener('click', checkedRadio)
        button.addEventListener('click', gettingTotal)

     }



  }



  function gettingTotal()
  {
    let valueget=0;
    let values =document.querySelector("#itemJson");
    valueget = localStorage.getItem('mess_total_money');
    if (valueget== null){
      valueget=10;
    }
    values.value=valueget;
    //localStorage.clear();
  }



    //Navbar using w3school website ideas(responsive navbar)////////////////////////////
    function myFunction() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
          x.className += " responsive";
      } else {
          x.className = "topnav";
      }
  }
  ///////////////////////////////////////////////////////////////////////////////




  function checkedRadio()
   {
    var i =0;
    var rate=0;
    var total=0;
    var offer_type = "";

    var gets = document.getElementsByClassName("radio");
    var text="";
    for(i=0;i<gets.length;i++)
    {
      if(gets[i].checked ==true  ){
        text= gets[i].value;

        if(text == "offer-1")
        {

          $('#itemtotal').val("₹"+"2000");
          total=2000;
          offer_type="type1";
          localStorage.setItem('mess_total_money',total);
          localStorage.setItem('mess_offer_type',offer_type);


        }

        if(text == "offer-2")
        {

          $('#itemtotal').val("₹ ​"+"2500");
          total=2500;
          offer_type="type2";
          localStorage.setItem('mess_total_money',total);
          localStorage.setItem('mess_offer_type',offer_type);

        }

        if(text == "offer-3")
        {

          $('#itemtotal').val("₹ ​"+"3000");
          total=3000;
          offer_type="type3";
          localStorage.setItem('mess_total_money',total);
          localStorage.setItem('mess_offer_type',offer_type);

        }
      }
      else{

      }
    }

   }
