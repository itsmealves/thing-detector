import { Component, OnInit, ViewChild } from '@angular/core';
import { FileService } from '../file.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
    private done: boolean = true;

    @ViewChild('fileInput')
    private fileInput: any;

    constructor(private fileService: FileService) {}

    ngOnInit() {}

    public handleFileInput(files: FileList) {
        const file = files.item(0);

        const onSuccess = (response) => {
            console.log('success');

            setTimeout(() => {
                this.done = true;
            }, 1000);
        };

        const onError = (error) => {
            console.log(error);

            setTimeout(() => {
                this.done = true;
            }, 1000);
        }

        this.done = false;
        this.fileService.upload(file)
            .then(onSuccess)
            .catch(onError);

        this.fileInput.nativeElement.value = "";
    }
}
