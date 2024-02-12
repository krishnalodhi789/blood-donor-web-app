// ====================================
// Registration Page JS===========
// =================================
function counter(second){
	dis_sec=document.getElementById('otp_second')
	resend=document.getElementById('resend')
	resend.disabled=true
	if(second == -1){
			dis_sec.innerText=' OTP'
			resend.classList.add('btn-success','text-white','fw-bold')
			resend.classList.remove('btn-outline-primary')
			resend.disabled=false
		return 0
	}
	else{
		setTimeout(()=>{
			dis_sec.innerText=second
			second--
			counter(second)
		},1000)
	}
	
}


// ==================================================================
// Choose Blood Group form =========================================
// ==================================================================

function selected(value){
	listGroup = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
	for(let i=0; i<8; i++ ){
		if(value==listGroup[i]){
			document.getElementById('bloodgroup'+listGroup[i]).classList.add("active_group")
		}
		else{
			document.getElementById('bloodgroup'+listGroup[i]).classList.remove("active_group")
		}		
	}
	document.getElementById('user_blood').innerHTML=`<h1> {value} </h1>`

}