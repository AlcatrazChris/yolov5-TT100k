import os
# path_list=os.listdir(r'E:\Dataset\Dataset\images')
# print(len(path_list))
# with open('train.txt','w',encoding='utf-8') as fp:
#     i=0
#     for path in path_list:
#         i+=1
#
#
#         path=fr'E:\Dataset\Dataset\images\{path}'
#         fp.write(path)
#         fp.write('\n')
#         if i>8310:
#             break
list=['ph5','p26','pl40','pl60','pn','i5','p11','pne','pcl','pl50','w55','pl5','ph4.5','pl80','w30','pg','pl30','p19','i4l','i2r','pl35','pm20','pbp','p5','pl120','p13','w57','ip','p10','il100','il60','il90','pb','pl110','w59','il80','pl100','ph4','pmb','p14','pl15','p1','w21','w42','i4','p16','p3','pl70','pdd','w32','w13','i2','pr40','pm30','w63','p12','p17','p18','im','pl20','p6','p27','pr30','i12','wc','i10','p23','ps','w58','p25','ph3','pl90','pbm','ph3.3','pl10','pss','pm55','pm10','w47','pr60','il50','pr20','w22','iz','p9','pm15','w3','p29','pa14','ph4.2','pa13','pr50','w45','il110']
train_path=os.listdir(r"E:\Dataset\Dataset\images\train\labels")

for path in train_path:
    path=rf"E:\Dataset\Dataset\images\train\labels\{path}"
    with open(path,'r') as fp:
        real_lines=""
        e_lines=fp.readlines()
        for line in e_lines:

            tag,t1,b1,t2,b2=line.split(' ')
            t1=float(t1)
            t2=float(t2)
            b1=float(b1)
            b2=float(b2)
            cx=(t2+t1)/(2*2048)
            cy=(b2+b1)/(2*2048)
            w=(t2-t1)/2048
            h=(b2-b1)/2048
            real_lines+=f'{tag} {cx} {cy} {w} {h}\n'
    fp.close()
    with open(path,'w') as fp:
        fp.write(real_lines)





