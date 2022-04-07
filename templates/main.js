

      function getvalues(){
      
        var selected=new Array();
        var chkbox=document.getElementById("tab1");
        var selected_check=document.getElementsByName('chk_dis')
        
        for(var i=0;i<selected_check.length;i++)
        {
          if(selected_check[i].checked)
            {
               selected.push('1');
            }
            else
            {
              selected.push('0');
            }
        
        }
        console.log(selected);
        }