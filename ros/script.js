// ros connection
var ros = new ROSLIB.Ros({
  url: 'ws://192.168.3.9:8080/'
});

// definiton of topic publisher
topic_publisher = new ROSLIB.Topic({
  ros:ros,
  name:'/topic_test',
  messageType:'std_msgs/Int16MultiArray',
});


// initialize variables
var value_a = 99;
var value_b = 0;

// function of publish topic
function ros_topic_pub(value_a, value_b){
  var ros_topic = new ROSLIB.Message({
    data:[value_a, value_b]
  });
  topic_publisher.publish(ros_topic);
}


// set interval
function rostopic_publish_loop(){
  setInterval('ros_topic_pub(value_a, value_b)', 100);
}

window.onload = function(){
  rostopic_publish_loop();
}




// definition of a topic subscriber
var ros_topic_sub = new ROSLIB.Topic({
  ros:ros,
  name:'./odom',
  messageType:'nav_msgs/Odometry',
})

ros_topic_sub.subscribe(function(message){
  var pose_x = message.pose.pose.position.x;
  var pose_y = message.pose.pose.position.y;
  
  var $baselink_x_showed = document.getElementById('pose_x_indicator');
  var $baselink_y_showed = document.getElementById('pose_y_indicator');

  $baselink_x_showed.innerHTML = 'x:' + pose_x + '[m]';
  $baselink_y_showed.innerHTML = 'y:' + pose_y + '[m]';
})
