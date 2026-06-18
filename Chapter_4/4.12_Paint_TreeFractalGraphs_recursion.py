import turtle as tt
def draw_brach(brach_length):
    if brach_length > 20:
        tt.forward(brach_length)
        tt.backward(brach_length)

        tt.forward(brach_length/3)
        tt.left(30)

        draw_brach(brach_length/2)
        tt.right(30)
        tt.backward(brach_length/3)

        # Middle branch
        tt.forward(brach_length/2)
        tt.right(30)
        draw_brach(brach_length/2)
        tt.left(30)
        tt.backward(brach_length/2)


        # Upper branch
        tt.forward(brach_length*2/3)
        tt.left(30)
        draw_brach(brach_length/2)
        tt.right(30)
        tt.backward(brach_length*2/3)
    
tt.left(90)
tt.penup()
tt.backward(150)
tt.pendown()
tt.color("green")
draw_brach(400)
tt.exitonclick()
