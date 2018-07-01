import { Component, OnInit, ViewChild } from '@angular/core';
import { FileService } from '../file.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
    private done: boolean = true;
    private url: string = '';
    private key: string = '';
    private queryKey: string = '';

    @ViewChild('fileInput')
    private fileInput: any;

    constructor(private fileService: FileService) {}

    ngOnInit() {}

    public query() {
        this.done = false;
        this.fileService.query(this.queryKey)
            .then(this.serviceSuccess.bind(this))
            .catch(this.serviceFailure.bind(this));

        this.queryKey = '';
    }

    public updateImage(detection: any) {
        this.url = detection.url;
        this.key = detection.key;
    }

    public hasImage() {
        return this.url.length > 0;
    }

    public serviceSuccess(response) {
        this.updateImage(response);

        setTimeout(() => {
            this.done = true;
        }, 1000);
    }

    public serviceFailure(error) {
        console.log(error);

        setTimeout(() => {
            this.done = true;
        }, 1000);
    }

    public handleFileInput(files: FileList) {
        const file = files.item(0);

        this.done = false;
        this.fileService.upload(file)
            .then(this.serviceSuccess.bind(this))
            .catch(this.serviceFailure.bind(this));

        this.fileInput.nativeElement.value = "";
    }
}
