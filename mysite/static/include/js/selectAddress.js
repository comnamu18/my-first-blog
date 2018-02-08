
      var groups=document.frmLog.Address.options.length
      var group=new Array(groups)
      for (i=0; i<groups; i++)
      group[i]=new Array()

      <!---------- 아래와 같은 방법으로 각 항목을 설정 합니다 ---------------->
      // http://www.mmca.go.kr/juso_new/newZipAddr_jibun.jsp에서 찾음

      group[0][0]=new Option("전체","전체")
      group[0][1]=new Option("강남구","강남구")
      group[0][2]=new Option("강동구","강동구")
      group[0][3]=new Option("강북구","강북구")
      group[0][4]=new Option("강서구","강서구")
      group[0][5]=new Option("관악구","관악구")
      group[0][6]=new Option("광진구","광진구")
      group[0][7]=new Option("구로구","구로구")
      group[0][8]=new Option("금천구","금천구")
      group[0][9]=new Option("노원구","노원구")
      group[0][10]=new Option("도봉구","도봉구")
      group[0][11]=new Option("동대문구","동대문구")
      group[0][12]=new Option("동작구","동작구")
      group[0][13]=new Option("마포구","마포구")
      group[0][14]=new Option("서대문구","서대문구")
      group[0][15]=new Option("서초구","서초구")
      group[0][16]=new Option("성동구","성동구")
      group[0][17]=new Option("성북구","성북구")
      group[0][18]=new Option("양천구","양천구")
      group[0][19]=new Option("영등포구","영등포구")
      group[0][20]=new Option("용산구","용산구")
      group[0][21]=new Option("은평구","은평구")
      group[0][22]=new Option("종로구","종로구")
      group[0][23]=new Option("중구","중구")
      group[0][24]=new Option("중랑구","중랑구")

      group[1][0]=new Option("전체","전체") 
      group[1][1]=new Option("가평군","가평군") 
      group[1][2]=new Option("고양시","고양시")
      group[1][3]=new Option("과천시","과천시")
      group[1][4]=new Option("광명시","광명시")
      group[1][5]=new Option("광주시","광주시")
      group[1][6]=new Option("구리시","구리시")
      group[1][7]=new Option("군포시","군포시")
      group[1][8]=new Option("김포시","김포시")
      group[1][9]=new Option("남양주시","남양주시")
      group[1][10]=new Option("동두천시","동두천시")
      group[1][11]=new Option("성남시","성남시")
      group[1][12]=new Option("수원시","수원시") 

      group[2][0]=new Option("전체","전체")
      group[2][1]=new Option("강릉시","강릉시")
      group[2][2]=new Option("고성군","고성군")
      group[2][3]=new Option("동해시","동해시")
      group[2][4]=new Option("삼척시","삼척시")
      group[2][5]=new Option("속초시","속초시")
      group[2][6]=new Option("양구군","양구군")
      group[2][7]=new Option("양양군","양양군")
      group[2][8]=new Option("영월군","영월군")

      var temp=document.frmLog.secondAddress

      function redirect(x){
      for (m=temp.options.length-1;m>0;m--)
      temp.options[m]=null
      for (i=0;i<group[x].length;i++){
      temp.options[i]=new Option(group[x][i].text,group[x][i].value)
      }
      temp.options[0].selected=true
      }

      function go(){
      location=temp.options[temp.selectedIndex].value
      }