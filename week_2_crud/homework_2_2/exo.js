use students

var cur = db.grades.find({type:"homework"}).sort({student_id:true, score:1})
var myid = -1;

while(cur.hasNext()) { 
    var s = cur.next(); 

    if(s["student_id"]!=myid) {
        myid=s["student_id"]; 
        db.grades.remove({"_id" : s["_id"]})
    }
}