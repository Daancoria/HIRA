import React, { useState } from 'react';
import styles from '../pages/ChatbotPage.module.css';
import toast from 'react-hot-toast';

interface Props {
  onUploadSuccess: (fileName: string) => void;
}

export default function FileUploader({ onUploadSuccess }: Props) {
  const [isUploading, setIsUploading] = useState(false);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const validTypes = [
      'application/pdf',
      'application/vnd.ms-excel',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      'text/csv',
    ];

    if (!validTypes.includes(file.type)) {
      toast.error('❌ Unsupported file type.');
      return;
    }

    if (file.size > 2 * 1024 * 1024) {
      toast.error('❌ File too large. Max 2MB.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setIsUploading(true);
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const status = response.status;

        if (status === 413) {
          toast.error('❌ Upload failed: File too large.');
        } else if (status === 500) {
          toast.error('❌ Server error. Please try again later.');
        } else {
          toast.error(`❌ Upload failed. Status: ${status}`);
        }

        return;
      }

      onUploadSuccess(file.name);
      toast.success('✅ File uploaded successfully!');
    } catch (error: any) {
      console.error('Upload error:', error);

      if (error instanceof TypeError) {
        toast.error('❌ Network error. Check your connection.');
      } else {
        toast.error('❌ Unexpected error occurred.');
      }
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className={styles.uploadBox}>
      <label
        htmlFor="fileInput"
        className={styles.uploadLabel}
        style={{ opacity: isUploading ? 0.6 : 1 }}
      >
        📎 Upload KPI File (.csv, .xls, .pdf)
      </label>

      <input
        id="fileInput"
        type="file"
        accept=".csv,.xls,.xlsx,.pdf"
        onChange={handleFileUpload}
        className={styles.uploadInput}
        disabled={isUploading}
      />

      {isUploading && (
        <div style={{ marginTop: 8, fontSize: '0.9em', color: '#888' }}>
          ⏳ Uploading...
        </div>
      )}
    </div>
  );
}
