from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.userController import router as userRouter
from controller.userTypeController import router as userTypeRouter
from controller.authController import router as authRouter

app = FastAPI()

# Running local environment
origins = ["*"]

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(userRouter)
app.include_router(userTypeRouter)
app.include_router(authRouter)