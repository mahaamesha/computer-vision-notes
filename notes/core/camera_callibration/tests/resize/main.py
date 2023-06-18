import cv2 as cv
import matplotlib.pyplot as plt


def size_preconditioning(file_path, dsize:tuple=(1920,1080)):
    """
    Function to crop image into desired size (default=1920x1080).
    I assume that the input image has larger size.
    """
    im = cv.imread(file_path)
    h, w = im.shape[:2]

    # resize
    resize_size = (w, h)
    c = 1   # divider factor
    while resize_size[0] > dsize[0] and resize_size[1] > dsize[1]:
        c += 0.1
        resize_size = (int(w/c), int(h/c))
        print(f'c={c}\tsize={resize_size}')
        if resize_size[0] < dsize[0] or resize_size[1] < dsize[1]:  # in last iteration
            c -= 0.1
            resize_size = (int(w/c), int(h/c))
            print(f'c={c}\tsize={resize_size}')
            h, w = resize_size[1], resize_size[0]
            break
    im_resize = cv.resize(im, resize_size)

    # rows n cols range for cropping
    rows = (h//2-dsize[1]//2, h//2+dsize[1]//2)    # rows ~ height
    cols = (w//2-dsize[0]//2, w//2+dsize[0]//2)    # cols ~ width
    im_crop = im_resize[rows[0]:rows[1], cols[0]:cols[1]]

    im_final = cv.rectangle(im_resize.copy(), pt1=(cols[0], rows[0]), pt2=(cols[1], rows[1]), color=(0,255,0), thickness=int(0.5/100*h))
    im_final = cv.circle(im_final, (w//2, h//2), color=(0,255,0), radius=int(1/100*h), thickness=-1)
    
    plt.subplot(221); plt.title('original'); plt.imshow(cv.cvtColor(im, cv.COLOR_BGR2RGB))
    plt.subplot(222); plt.title('resized'); plt.imshow(cv.cvtColor(im_resize, cv.COLOR_BGR2RGB))
    plt.subplot(223); plt.title('croped'); plt.imshow(cv.cvtColor(im_crop, cv.COLOR_BGR2RGB))
    plt.subplot(224); plt.title('final'); plt.imshow(cv.cvtColor(im_final, cv.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.savefig(r'tests\resize\im_final.jpg', dpi=300)
    plt.show()

    return im_crop


if __name__ == '__main__':
    file_path = r'tests\resize\DSC_2955.JPG'

    size_preconditioning(file_path, dsize=(1920,1080))