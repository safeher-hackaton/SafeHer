import { Body, Controller, Post } from "@nestjs/common";
import { AppService } from './app.service';
import { Observable } from "rxjs";

@Controller('api')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post()
  register(@Body() user: any): Observable<any> {
    return this.appService.registerUser(user);
  }
}
