import cv2 

def embedlogo(img_path, logo_path):
    # img_path = './img/uq_river_picasso_5.jpg'
    # logo_path = './logo/mm_logo.jpg'
    # out = './temp.jpg'
    out = './img/'+img_path.split('/')[2][:-4]+'_logo'+img_path.split('/')[2][-4:]
    img = cv2.imread(img_path)
    if logo_path.split('.')[-1]=='png':
        logo = cv2.imread(logo_path, -1)
        logo = logo[:,:,:3]
    else:
        logo = cv2.imread(logo_path)
    w,h,c = img.shape
    lw,lh,lc = logo.shape
    # resized = cv2.resize(logo, (lw//2, lh//2), interpolation = cv2.INTER_AREA)
    for i in range(lw):
        for j in range(lh):
            if logo[i,j,0] < 128 and logo[i,j,1] < 128 and logo[i,j,2] < 128:
                img[1080-lw+i,1080-lh+j,:] = logo[i,j,:]
    cv2.imwrite(out, img)
    return out