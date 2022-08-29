extends KinematicBody2D //This is what to apply the script to
var velocity = Vector2(0,0) ##vector2 is the 2D equivalent for physics only needs two coordinates X and Y
var gravity = 2000 //variable for gravity
func _physics_process(delta): //function for physics that updates on delta
	
	 if Input.is_action_pressed("left_arrow"): //if left arrow is pressed
			velocity.x = -200                      //Move the sprite with a velocity of -200 on the x axis
			$AnimatedSprite.play("run")            //play animated sprite 'run' 
			$AnimatedSprite.flip_h = true          //flip the sprite horizontally
			
	 elif Input.is_action_pressed("right_arrow"): //This one is the opposite so that when the right arrow is pressed 
			velocity.x = 200                          //velocity x is 200 play animation run don't flip
			$AnimatedSprite.play("run")
			$AnimatedSprite.flip_h = false
			
	 else:
			$AnimatedSprite.play("idle") //otherwise play the idle animation
			
	 velocity.y = velocity.y + gravity * (delta) //This adds the gravity variable then makes the y velocity a multiple of of delta
	 move_and_slide(velocity) //I didn't quite get this but found a comment that makes sense "You need to save the new velocity after 
	 velocity.x = lerp(velocity.x,0,0.1) // move_and_slide does its magic because you're going to pass it to move_and_slide again next frame.
                                       // Otherwise the velocity would never change between frames except via input. velocity.x = lerp(velocity.x,0,0.1)
##Original script                      // this line above is linear interpolation which works like friction interpolating between 0 and .1

extends KinematicBody2D
var velocity = Vector2(0,0)
var gravity = 2000
func _physics_process(delta):
	
	 if Input.is_action_pressed("left_arrow"):
			velocity.x = -200
			$AnimatedSprite.play("run")
			$AnimatedSprite.flip_h = true
			
	 if Input.is_action_pressed("right_arrow"): //this part of the script wouldn't work properly unless changed to elif
			velocity.x = 200                       // everything would work as normal but the animation wouldn't play.
			$AnimatedSprite.play("run")            //This made it a little hard to diagnose what was wrong, but I eventually figured it out
			$AnimatedSprite.flip_h = false
			
	 else:
			$AnimatedSprite.play("idle")
			
	 velocity.y = velocity.y + gravity * (delta)
	 move_and_slide(velocity)
	 velocity.x = lerp(velocity.x,0,0.1)
