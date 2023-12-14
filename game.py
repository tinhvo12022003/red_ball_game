import pygame 
import sys
import random 

pygame.init()

screen = pygame.display.set_mode((800, 600)) #khởi tạo cửa sổ game
pygame.display.set_caption("Red Ball Game")

background = pygame.image.load("img/bg1.gif") #load background
background = pygame.transform.scale(background, (800, 600)) #resize basckground vừa với khung cửa sổ

red_ball = pygame.image.load("img/red_ball.png").convert_alpha() #load red ball
red_ball = pygame.transform.scale(red_ball, (50, 50))
'''
set vị trí bắt đầu cho red ball
+ ball_x_start = 800/2 = 400
+ ball_y_start = 600/2 = 300 
'''
ball_x_start = 400
ball_y_start = 100


wood_floor = pygame.image.load("img/wood_floor.png").convert_alpha() #load wood floor
wood_floor_index = 1.5

clock = pygame.time.Clock() #khởi tạo đồng hồ 

gavity = 1.5 #trọng lực kéo red ball


spawn_wood_floor = pygame.USEREVENT #set sự kiện cho spawn
pygame.time.set_timer(spawn_wood_floor, 500) #thiết lập thời gian xuất hiện cho wood floor
lst_wood_floor = []
lst_wood_floor_pos = [200, 400, 600] #mảng chứa các giá trị position ngẫu nhiên khi xuất hiện

''''''''''''''
' function   '
''''''''''''''

def create_wood_floor(): #hàm tạo wood floor
    wood_floor_rect = wood_floor.get_rect(midbottom=(random.choice(lst_wood_floor_pos), 600))
    return wood_floor_rect
    
def end_game() -> bool:
    if ball_y_start <= 0: return False
    if ball_y_start >= 600: return False
    return True

while True:
    #xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #thoát game
            sys.exit()
        if event.type == spawn_wood_floor: #vẽ các wood floor sau mỗi timer
            lst_wood_floor.append(create_wood_floor())
            
        #xử lý sự kiện cho phím điều hướng
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            ball_x_start -= 3
        if event.key == pygame.K_RIGHT:
            ball_x_start += 3
          


    screen.blit(background, (0, 0)) #vẽ background lên cửa sổ

    ball_y_start += gavity  #set ball_y mỗi dòng while cộng thêm gavity làm red ball đi xuống
    screen.blit(red_ball, (ball_x_start, ball_y_start)) #vẽ red ball lên cửa sổ


    for wood in lst_wood_floor: #di chuyển trục y của wood floor
        wood.y -= wood_floor_index
        screen.blit(wood_floor, wood)

        if wood.colliderect(red_ball.get_rect(center=(ball_x_start, ball_y_start))):
            ball_y_start = wood.top


    if(not end_game()):
        print("Game Over")
        pygame.quit() #thoát game
        sys.exit()


    pygame.display.update()
    clock.tick(240)