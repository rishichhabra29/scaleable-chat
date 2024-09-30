import {Server} from "socket.io"
import Redis from 'ioredis'
import prismaClient from "./prisma";

const pub=new Redis({
    host: 'caching-3b1b9c5f-chhabrarishi2001-0b95.h.aivencloud.com',
    port: 22604,
    username: 'default',
    password: 'AVNS_iTynHSSCDFFyfqOTQsr',
});
const sub=new Redis({
    host: 'caching-3b1b9c5f-chhabrarishi2001-0b95.h.aivencloud.com',
    port: 22604,
    username: 'default',
    password: 'AVNS_iTynHSSCDFFyfqOTQsr',

});



class SocketService {
    private _io: Server;
      constructor(){
          console.log("INIT Socket Service...");
          this._io=new Server({
              cors:{
                  allowedHeaders: ["*"],
                  origin: "*",
  
              },
          });
          sub.subscribe('MESSAGES')
      }
      public initListeners() {
          const io=this.io;
          console.log('Init Sockets Listeners....');
          io.on("connect",(socket)=>{
              console.log(`New Socket Connected `,socket.id);
              socket.on("event:message",async({message}:{message:string})=>{
                  console.log("New message Rec.",message);
                  await pub.publish("MESSAGES",JSON.stringify({message}));
  
  
              });
  
          });
          sub.on('message',async (channel,message)=>{
              if(channel==='MESSAGES'){
                  console.log('new message from redis',message)
                  io.emit("message",message);
                  await prismaClient.message.create({
                    data:{
                        text: message,
                    }
                  })
              }
          });
          
      }
      get io() {
          return this._io;
      }
  }
  export default SocketService;
